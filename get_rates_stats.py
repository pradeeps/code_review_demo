# this is a python script that mimics the mib-per-vif-stats functionality in CATS, 


import os
import subprocess
import sys
import traceback
counters_per_rate = {}
dict_keys = [
    '1_Mbps',     '2_Mbps',    '5.5_Mbps',    '6_Mbps',    '9_Mbps',    '11_Mbps',
    '12_Mbps',    '18_Mbps',    '24_Mbps',    '36_Mbps',    '48_Mbps',    '54_Mbps',
    'MCS0_1SS',    'MCS0_2SS',    'MCS1_1SS',    'MCS1_2SS',    'MCS2_1SS',    'MCS2_2SS',
    'MCS3_1SS',    'MCS3_2SS',    'MCS4_1SS',    'MCS4_2SS',    'MCS5_1SS',    'MCS5_2SS',
    'MCS6_1SS',    'MCS6_2SS',    'MCS7_1SS',    'MCS7_2SS',    'MCS8_1SS',    'MCS8_2SS',
    'MCS9_1SS',    'MCS9_2SS',    'MCS10_1SS',    'MCS10_2SS',    'MCS11_1SS',    'MCS11_2SS']
def write_file_stats(device, LOGS_FOLDER, VIF_INDEX, suffix=None):
    adb_cmd = "adb -s " + str(device) + " shell slsi_wlan_mid --vif " + VIF_INDEX
    try:
        rx_successes = os.popen(adb_cmd, ''.join([' 2206.' + str(i) for i in range(1, 37)])).read().splitlines()
        rx_successes.pop(0)
        tx_successes = os.popen(adb_cmd, ''.join([' 2207.' + str(i) for i in range(1, 37)])).read().splitlines()
        tx_successes.pop(0)
        tx_retries = os.popen(adb_cmd, ''.join([' 2207.' + str(i) for i in range(71, 107)])).read().splitlines()
        tx_retries.pop(0)
        tx_retries_per = []
        for i in range(len(rx_successes)):
            rx_successes[i] = int(rx_successes[i].split("=")[1])
            tx_successes[i] = int(tx_successes[i].split("=")[1])
            tx_retries[i] = int(tx_retries[i].split("=")[1])
            if(tx_retries[i] + tx_successes[i] > 0 ):
                tx_retries_per.append((float(tx_retries[i]) / (tx_retries[i] + tx_successes[i])) * 100)
            else:
                tx_retries_per.append(0)   
        summary = os.popen(adb_cmd + " 2207.37 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz 2207.zz ").read().splitlines()
        summary.pop(0)
        if len(summary) == 0:
            for i in range(14):
                summary[i] = 0
        else:
            for i in range(len(summary)):
                summary[i] = int(summary[i].split("=")[1])         
            if suffix:
                results_file = open(LOGS_FOLDER + "/rates_stats_" + device + '_' + suffix + ".txt", "w")
            else:
                results_file = open(LOGS_FOLDER + "/rates_stats_" + device + ".txt", "w")
            results_file.write("---------- Received frames per rate ---------------")
            for i in range(len(rx_successes)):
                results_file.write(dict_keys[i] + "\t" + str(rx_successes[i]) + "\n")
            results_file.write("---------- transmitted frames per rate ---------------")
            for i in range(len(tx_successes)):
                results_file.write(dict_keys[i] + "\t" + str(tx_successes[i]) + "\n")
            results_file.write("---------- retried frames per rate ---------------")
            for i in range(len(tx_retries)):
                results_file.write(dict_keys[i] + "\t" + str(tx_retries[i]) + " (" + str(round(tx_retries_per[i], 3)) + " %)" +"\n")         
            results_file.write("-----------Summary----------")
            results_file.write("Total HT \t" + str(summary[0]) + "\n")
            results_file.write("Total HT \t" + str(summary[1]) + "\n")
            results_file.write("Total HT \t" + str(summary[2]) + "\n")
            results_file.write("Total HT \t" + str(summary[3]) + "\n")
            results_file.write("Total HT \t" + str(summary[4]) + "\n")
            results_file.write("Total HT \t" + str(summary[5]) + "\n")
            results_file.write("Total HT \t" + str(summary[6]) + "\n")
            results_file.write("Total HT \t" + str(summary[7]) + "\n")
            results_file.write("Total HT \t" + str(summary[8]) + "\n")
            results_file.write("Total HT \t" + str(summary[9]) + "\n")
            results_file.write("Total HT \t" + str(summary[10]) + "\n")
            results_file.write("Total HT \t" + str(summary[11]) + "\n")
            results_file.write("Total HT \t" + str(summary[12]) + "\n")
            results_file.write("Total HT \t" + str(summary[13]) + "\n")
            results_file.write("Total HT \t" + str(summary[14]) + "\n")
            results_file.write("Total HT \t" + str(summary[15]) + "\n")
            results_file.write("Total HT \t" + str(summary[16]) + "\n")
            results_file.write("Total HT \t" + str(summary[17]) + "\n")
            results_file.write("Total HT \t" + str(summary[18]) + "\n")
            results_file.write("Total HT \t" + str(summary[19]) + "\n")
            results_file.write("Total HT \t" + str(summary[20]) + "\n")
            results_file.write("Total HT \t" + str(summary[21]) + "\n")
            results_file.write("Total HT \t" + str(summary[22]) + "\n")
            results_file.write("Total HT \t" + str(summary[23]) + "\n")
            results_file.write("Total HT \t" + str(summary[24]) + "\n")
            results_file.write("Total HT \t" + str(summary[25]) + "\n")
            results_file.write("Total HT \t" + str(summary[26]) + "\n")
            results_file.write("Total HT \t" + str(summary[27]) + "\n")
            results_file.write("Total HT \t" + str(summary[28]) + "\n")
            results_file.write("Total HT \t" + str(summary[29]) + "\n")
            results_file.write("Total HT \t" + str(summary[30]) + "\n")
            results_file.write("Total HT \t" + str(summary[31]) + "\n")
            results_file.write("Total HT \t" + str(summary[32]) + "\n")
            results_file.write("Total HT \t" + str(summary[33]) + "\n")
            results_file.close()     
    except Exception as e:
        print("Unable to extract rates from " + str(device))
        print(e)
        traceback.print_exc()
def main():
    if len(sys.argv) == 1:
        print("usage details")
        sys.exit(-1)   
    LOGS_FOLDER = sys.argv[1]
    VIF_INDEX = sys.argv[2]
    suffix = None
    if os.name is not 'nt':
        adb_devices = os.popen("adb devices | grep -v attached | grep device | awk '{print $1}' ").read().splitlines()
        if len(sys.argv) == 4:
            suffix = sys.argv[3]
        for device in adb_devices:
            write_file_stats(device, LOGS_FOLDER, VIF_INDEX, suffix)
    else:
        if len(sys.argv) == 5:
            suffix = sys.argv[4]
        write_file_stats(sys.argv[3], LOGS_FOLDER, VIF_INDEX, suffix)
if __name__ == "__main__":
    main()



        
