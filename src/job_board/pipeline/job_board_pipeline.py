# from database.postgres import PostgresDB
from job_board.etl.extract import Extract
from job_board.etl.transform import Transform
from job_board.etl.load import Load
#from utility.metadata_logging import something
import os 
import logging
import yaml 
from io import StringIO
from utility.metadata_logging import MetadataLogging
import datetime as dt
from apscheduler.schedulers.background import BackgroundScheduler   
import time


def pipeline_per_job_title():
    '''
    docstring here
    '''
    
    # start the streamIO from a clean slate 
    # run_log.seek(0)
    # run_log.truncate(0)

    api_key_id = "5fec918ab1msh2089eaf59c35a4fp1d2106jsnc87acf303a5f"
    # api_key_id = os.environ.get("api_key_id")

    # metadata_logger = MetadataLogging()
        
    # metadata_logger_table = f"metadata_log_{config['load']['database']['target_table_name']}"
    # metadata_logger_run_id = metadata_logger.get_latest_run_id(db_table=metadata_logger_table)
    # metadata_logger.log(
    #     run_timestamp=dt.datetime.now(),
    #     run_status="started",
    #     run_id=metadata_logger_run_id, 
    #     run_config=config,
    #     db_table=metadata_logger_table
    # )

    # logging.info(f"Commencing pipeline for {config['extract']['stock_ticker']}⏳")
    # logging.info("Commencing extraction")
    # extract data 
    try:
        
        df = Extract.extract(
            job_title=config["extract"]["title"], 
            api_key_id=api_key_id
        )
        logging.info(f"Extraction complete for job title : {config['extract']['title']}")

        logging.info("Commencing transformation")
        # transform data
        df_transform = Transform.transform(
            title_list=title_list,
            request_id_list=request_id_list,
            df_list=df_list
        )
        logging.info("Transformation complete")

        # load file (upsert)
        logging.info("Commencing file load")
        Load.load(
            df=df_transform,
            load_target=config["load"]["file"]["load_target"],
            target_file_directory=config["load"]["file"]["target_file_directory"],
            target_file_name=config["load"]["file"]["target_file_name"],
        )   
        logging.info("File load complete")

        engine = PostgresDB.create_pg_engine()

        # load database (upsert)
        logging.info("Commencing database load")
        Load.load(
            df=df_transform,
            load_target=config["load"]["database"]["load_target"],
            target_database_engine=engine,
            target_table_name=config["load"]["database"]["target_table_name"]
        )  
        logging.info("Database load complete")
        logging.info(f"Pipeline for {config['extract']['stock_ticker']} complete ✅")

        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="completed",
            run_id=metadata_logger_run_id, 
            run_config=config,
            run_log=run_log.getvalue(),
            db_table=metadata_logger_table
        )
        
        
        return True
    except BaseException as e: 
        logging.exception(e)
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="error",
            run_id=metadata_logger_run_id, 
            run_config=config,
            run_log=run_log.getvalue(),
            db_table=metadata_logger_table
        )
    print(run_log.getvalue())

def pipeline()->bool:
    print("job running")
    run_log = StringIO()
    logging.basicConfig(level=logging.INFO, stream=run_log,format="[%(levelname)s][%(asctime)s][%(filename)s]: %(message)s") # format: https://docs.python.org/3/library/logging.html#logging.LogRecord
    # get yaml config 
    with open("job_board/config.yaml") as stream:
        config = yaml.safe_load(stream)

    for job_title in config["job_titles"]:
        pipeline_per_job_title(config=job_title['job_title'], run_log=run_log)
    
    return True 


if __name__ == "__main__": 
    
    # run the pipeline
    if pipeline():
        print("success")