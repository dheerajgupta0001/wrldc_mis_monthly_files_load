from src.config.appConfig import getFileMappings
from src.DataFetcher.statesDailyDataFetcher import getStatesDailyData
import datetime as dt

# TODO delete this
def getGenLinesDailyData():
    fileObjs = getFileMappings()
    getStatesDailyData(fileObjs[2], dt.datetime(2021,1,1), 0 )