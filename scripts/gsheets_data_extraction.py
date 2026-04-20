# Importação das bibliotecas necessárias
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
import numpy as np
from datetime import date
from datetime import timedelta
import hashlib
from pymongo import UpdateOne
from pymongo.mongo_client import MongoClient