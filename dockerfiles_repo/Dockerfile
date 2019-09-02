FROM 309544246384.dkr.ecr.cn-northwest-1.amazonaws.com.cn/python-3.6-alpine:init
COPY . .
RUN pip install -r requirements.txt -i  http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
