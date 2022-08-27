#remove Pandas future warnings
import warnings
warnings.simplefilter(
    action="ignore",
    category=FutureWarning
)
#general imports
from func_get_roundings import get_price_rounding
from config_execution_api import signal_positive_ticker
from config_execution_api import signal_negative_ticker
from func_position_calls import open_position_confirmation
from func_position_calls import active_position_confirmation
from func_trade_management import manage_new_trades
from func_execution_calls import set_leverage
from func_close_positions import close_all_positions
from func_save_status import save_status
from func_get_ZScore import get_latest_zscore
import time
import json

if __name__ == "__main__":
     #print a start signal to show script has launched
    print('Statbot Launched successfully.')


    #initialise Variables
    status_dict = {"message":"starting..."}
    order_long = {}
    order_short = {}
    signal_sign_positive = False
    signal_side = ""
    kill_switch = 0                            #<<< While killswitch is 0, trading is active. when kill_switch is = 1, trading is halted.

    #save Status
    save_status(status_dict)

    #Set Leverage:
    print('\n1.---Setting Leverage:---\n')
    set_leverage(signal_positive_ticker)
    set_leverage(signal_negative_ticker)

    #commence bot:
    print("\n\t2.---Seeking Trades:---")
    loop_count = 0
    while True:
        loop_count +=1

        #add time limit to protect API calling
        time.sleep(1)

        #check if open trades already exist
        is_p_ticker_open = open_position_confirmation(signal_positive_ticker)
        is_n_ticker_open = open_position_confirmation(signal_negative_ticker)
        is_p_ticker_active = active_position_confirmation(signal_positive_ticker)
        is_n_ticker_active = active_position_confirmation(signal_negative_ticker)
        checks_all = [is_n_ticker_active, is_p_ticker_active, is_n_ticker_open, is_p_ticker_open]

        print("\n\t__________Pre-Trade Checks:__________")
        print("\tis_n_ticker_active   :", is_n_ticker_active)
        print("\tis_p_ticker_active   :", is_p_ticker_active)
        print("\tis_n_ticker_open     :", is_n_ticker_open)
        print("\tis_p_ticker_open     :", is_p_ticker_open)
        print("\n\tKill Switch          :", kill_switch)
        try:
            coint_flag, zscore, signal_sign_positive = get_latest_zscore()
            print("\tZScore               :", zscore)
        except:
            print("coint_flag, zscore, signal_sign_positive = get_latest_zscore(): Error Occured")


        is_manage_new_trades = not any(checks_all) #<< this checks for if there are any trades or orders open. if there are, it assumes that a trade is active.

        #save status
        status_dict["message"] = "Initial checks made..."
        status_dict["checks"] = checks_all
        save_status(status_dict)
        print("\n\tStatus updated. \n____________________")


        #Check for signal and place new trades
        if is_manage_new_trades == True and kill_switch == 0:
            status_dict["message"] = "Looking for new trades..."
            save_status(status_dict)
            kill_switch, signal_side = manage_new_trades(kill_switch) # << This is where the killswitch is determined for the remainder of the script
            print(f"Following Manage_new_trades func, kill_switch is now: {kill_switch}")
            if kill_switch == 0:
                print(f"killswitch: {kill_switch}.There should be no active trades.")
            elif kill_switch == 1:
                print(
                    f"killswitch: {kill_switch}.There should be some active trades.")
            elif kill_switch == 2:
                print(
                    f"killswitch: {kill_switch}. All trades should be closing or closed.")


        #Managing open kill-switch position
        if kill_switch == 1:

            # get and save the latest zscore
            coint_flag, zscore, signal_sign_positive = get_latest_zscore()
            print(f"\tCurrent zscore:            {zscore}")

            #Close positions
            if signal_side == "positive" and zscore < 0:
                kill_switch = 2

            if signal_side == "negative" and zscore >= 0:
                kill_switch = 2

            # killswitch must be put back to zero if all trades are closed, so new trades can reopen.
            if is_manage_new_trades and kill_switch != 2:
                kill_switch = 0

        #Killswitch = 2 means we need to close all active orders and positions
        if kill_switch == 2:
            print("Closing all positions.")
            status_dict["message"] = "Closing all positions..."
            save_status(status_dict)
            kill_switch = close_all_positions(kill_switch)

        #sleep for a period of time before cycling through again.
        print(f"Loop count: {loop_count}")
        time.sleep(2)






