from google.cloud import storage
import os

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np


def initialize_bucket(credentials_path, bucket_name, create_bucket=False):
    '''
    function to access the data stored in a Google Storage bucket
    IN:
    credentials_path: local where the JSON file with the credentials is stored
    create_bucket: if the bucket needs to be created
    bucket_name: name of the bucket that is going to be accessed

    OUT:
    client: client initialized
    bucket: 
    '''

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    if create_bucket:
        bucket.location = 'US-EAST1'
        bucket.create()

    return client, bucket


def plot_importance(data, feature, title=None ,rows=15):
    '''
    INPUT:
    data - dataframe based on which the plot will be done
    feature - feature to plot
    title - plot title, default=None
    rows - number of rows to show
    '''
    corr_abs = data.iloc[:rows]
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(5,10), dpi=200)#, sharey=True)
    gs = fig.add_gridspec(1, 3)

    sns.heatmap(corr_abs, annot=True, cmap='magma_r', cbar=False,ax=ax[0])
    sns.barplot(x=feature, y=corr_abs.index, data=corr_abs, palette="magma")

    ax[0].axes.get_xaxis().set_visible(False)
    ax[1].axes.get_xaxis().set_visible(False)
    ax[1].axes.get_yaxis().set_visible(False)

    fig.suptitle(title, fontsize=20)
    sns.despine(bottom=True)