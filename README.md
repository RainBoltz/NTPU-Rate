# NTPU-Rate

A demo that shows some analytic results from social media (currently Facebook).  
Data crawled by Facebook Graph API, target fanspage: [靠北北大](https://www.facebook.com/NTPUhate/)

## TODO List
- [x] view: a website for presentation
- [ ] analyze: functions used to analyze data for further applications
- [ ] crawler: data streaming utilities

## Requirements
- python >= 3.5
- tornado >= 5.0

## Run server
1. go to directory above the three folders
    ```cmd
    cd NTPU-Rate\
    ```
    
2. type in `python view/startserver.py <start-time> <end-time> <port>`, for example:
    ```cmd
    python view/startserver.py 2017-01-01 2017-10-30 8888
    ```
    
3. open the website with link: `http://127.0.0.1:<port>`

## notes
- to view results in other timelines, you have to:
    1. crawl the data of `2018-01-01` to `2018-12-01`
    2. create a json file in correct format (as in the [source](https://github.com/RainBoltz/NTPU-Rate/tree/master/view))
    3. name the file name into `[SOURCE]-[ANALYSIS_TARGET]-[METHOD]_[start-time]_[end-time]` ([example](https://github.com/RainBoltz/NTPU-Rate/tree/master/view))
    4. dump to `json` files