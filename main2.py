from serialsimple import SerialLogger
from datetime import datetime

def main():

    port='/dev/ttyACM0'
    baudrate=115200
    log_interval_sec=120
    log_directory='logfiles'
    zip_directory='zipfiles'
    bucket_name = 'blackboxlinkedcar'
    s3_prefix = datetime.now().strftime('logfiles/%Y/%m/%d/%H/')
    timer = 600
    
    logger = SerialLogger(port, baudrate, log_interval_sec, log_directory, zip_directory, bucket_name, s3_prefix, timer)
    logger.start_logging()

if __name__ == '__main__':
    main()