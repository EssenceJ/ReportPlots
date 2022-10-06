import os  # library for managing directories
import glob  # library used to find files and pathnames that matches a pattern.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import mplcursors
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


# Defining function
def two_axis_plot(data, fileName, x, y, fig_title, x_label, y_label, ch):
    sns.set(style="darkgrid")
    date_title = (data['date'][0])
    channel = str(ch)
    # Setting plot size
    length = 40
    width = 20
    marker_size = 5
    font = 15

    # Setting frequency of ticks
    start = 0
    end = (len(data))  # size of data frame
    interval = 20
    x_ticks = np.arange(start, end, interval)
    angle = 45

    # two axis plot
    fig, ax = plt.subplots(figsize=(length, width))
    scatter = ax.scatter(x, y, s=marker_size)
    ax.set_facecolor('whitesmoke')
    ax.set_title(fig_title + ' CH' + channel + ' ' + date_title, fontsize=font)  # (fig_title + date_title)
    ax.set_xlabel(x_label, fontsize=font)
    ax.set_ylabel(y_label, fontsize=font)
    plt.xticks(x_ticks, rotation=angle)  # Changing the frequency of x ticks
    plt.grid(axis='y')

    # hover annotations
    mplcursors.cursor(scatter)  # or just mplcursors.cursor()

    # plt.show()#method for displaying plot
    # Save file

    # print(fileName[15:14])
    naming_conv = (fileName[15:14] + '_CH' + channel + '_' + x_label + '_' + y_label)  # Naming convention: Channel_file name_columns
    # saved = (saved_path + '\CH_' + channel + '_' + fileName + '_' + x_label + '_' + y_label)  # Naming convention: Channel_file name_columns
    # saved = saved_path
    fig.savefig(naming_conv, bbox_inches="tight")
    plt.close()
    plt.clf()


# Function for multiple axex
def multi_axes_plots(data, fileName, x, y1, y2, y3, fig_title, x_label, y1_label, y2_label, y3_label, ch):
    # 3 axis plots by time: 1)time by inputPowerRaw_LR_CH1(Oranage) 2)time by Signal to Noise(blue) 3) time by J RSD_frames(red)
    date_title = (data['date'][0])
    channel = str(ch)

    # Setting plot size
    length = 50
    width = 30
    marker_size = 2
    # font = 15

    # Setting frequency of ticks
    start = 0
    end = (len(data))  # size of data frame
    interval = 20
    x_ticks = np.arange(start, end, interval)
    angle = 45

    fig, ax1 = plt.subplots(figsize=(length, width))
    plt.xticks(x_ticks, rotation=angle)  # Changing the frequency of x ticks

    ax1.scatter(x, y1, s=marker_size, color='darkorange')

    ax2 = ax1.twinx()
    ax2.scatter(x, y2, s=marker_size, color='b')

    ax3 = ax1.twinx()
    ax3.scatter(x, y3, s=marker_size, color='red')
    ax3.spines['right'].set_position(('axes', 1.1))

    # set axis label
    ax1.set_ylabel(y1_label, color='darkorange')
    ax2.set_ylabel(y2_label, color='b')
    ax3.set_ylabel(y3_label, color='red')
    ax1.set_xlabel(x_label)
    ax1.set_title(fig_title + ' CH' + channel + ' ' + date_title)

    # set tick color
    ax1.tick_params(axis='y', colors='darkorange')
    ax2.tick_params(axis='y', colors='b')
    ax3.tick_params(axis='y', colors='red')

    # set spine color
    ax1.spines['left'].set_color('darkorange')
    ax2.spines['right'].set_color('b')
    ax3.spines['right'].set_color('red')

    # note: add legend

    # plt.show()#method for displaying plot
    # Save file

    saved = (saved_path + channel + '_' + fileName + '_' + x_label + '_' + y1_label + '_' + y2_label + '_' + y3_label)  # Naming convention: Channel_file name_columns
    fig.savefig(saved, bbox_inches="tight")
    fig.close()


# ************************************************************************************************************************************

# use glob to get all the csv files in the folder
path = input("Enter directory path:")  # allow user to input path

csv_files = glob.glob(os.path.join(path, "*.csv"))  # retrieves and joins different components of a path

# Counter for file name
# file_count=0


# loop over the list of csv files
for f in csv_files:
    # file_count +=1
    # read the csv file
    df = pd.read_csv(f)  # read_csv pandas method

    # print the location and filename
    # print('Location:', f)
    print('File Name:', f.split("\\")[-1])  # splits a string into a list of data
    file_name = (str(f.split("\\")[-1])[:-4])

    # Store desire column's data in a list
    time = df['date'].to_list()  # Date and Time
    az = df['az'].to_list()  # Azimuth
    alt = df['alt'].to_list()  # Altitude

    # Channel 1 columns
    StoN_CH1 = df['EbN0_LR_CH1'].to_list()  # Signal to Noise
    IPR_CH1 = df['inputPowerRaw_LR_CH1'].to_list()  # Input power
    RSD_framesP_CH1 = df['RSDFramesProcessed_LR_CH1'].to_list()  # RSD frames processed
    RSD_FramesUC_CH1 = df['RSDFramesUncorrectable_LR_CH1'].to_list()

    # Channel 2 columns
    StoN_CH2 = df['EbN0_LR_CH2'].to_list()  # Signal to Noise
    RSD_framesP_CH2 = df['RSDFramesProcessed_LR_CH2'].to_list()  # RSD frames processed
    RSD_FramesUC_CH2 = df['RSDFramesUncorrectable_LR_CH2'].to_list()

    # Function call

    # #Signal to Noise vs. Time CH 1
    two_axis_plot(data=df, fileName=file_name, x=time, y=StoN_CH1, fig_title='Signal to Noise vs. Time',
                  x_label='Time', y_label='Singal to Noise(dB)', ch=1)
    # #RSD Frames Processed vs. Time CH 1
    two_axis_plot(data=df, fileName=file_name, x=time, y=RSD_framesP_CH1, fig_title='RSD Frames Proccessed vs. Time',
                  x_label='Time', y_label='RSD Frames Proccessed', ch=1)
    # #RSD Frames Uncorrectable vs. Time Ch 1
    two_axis_plot(data=df, fileName=file_name, x=time, y=RSD_FramesUC_CH1,
                  fig_title='RSD Frames Uncorrectable vs. Time',
                  x_label='Time', y_label='RSD Frames Uncorrectable', ch=1)
    # Signal to Noise vs. Time CH 2
    two_axis_plot(data=df, fileName=file_name, x=time, y=StoN_CH2, fig_title='Signal to Noise vs. Time',
                  x_label='Time', y_label='Singal to Noise(dB)', ch=2)
    # RSD Frames Processed vs. Time CH 2
    two_axis_plot(data=df, fileName=file_name, x=time, y=RSD_framesP_CH2, fig_title='RSD Frames Proccessed vs. Time',
                  x_label='Time', y_label='RSD Frames Processed', ch=2)
    # RSD Frames Uncorrectable vs. Time Ch 2
    two_axis_plot(data=df, fileName=file_name, x=time, y=RSD_FramesUC_CH2,
                  fig_title='RSD Frames Uncorrectable vs. Time',
                  x_label='Time', y_label='RSD Frames Uncorrectable', ch=2)
    # Azimuth vs. Time
    two_axis_plot(data=df, fileName=file_name, x=time, y=az, fig_title='Azimuth vs. Time',
                  x_label='Time', y_label='Azimuth', ch=1)
    # Input Power vs. Time
    two_axis_plot(data=df, fileName=file_name, x=time, y=IPR_CH1, fig_title='Input Power vs. Time',
                  x_label='Time', y_label='Input Power(Raw)', ch=1)
    # Azimuth vs. Altitude
    two_axis_plot(data=df, fileName=file_name, x=az, y=alt, fig_title='Azimuth vs. Altitude',
                  x_label='Azimuth', y_label='Altitude', ch=1)

    # #multi_axis_plot(data = df, fileName = file_name, x = time, y1 = IPR_CH1, y2 = StoN_CH1, y3 = RSD_framesP_CH1,
    #                 #fig_title = 'Signal Strength, Signal to Noise and RSD Frames vs. Time', x_label = 'Time',
    #                 #y1_label = 'Input Power Raw', y2_label = 'Signal to Noise', y3_label = 'RSD Frames',ch = 1 )

print('completed')
