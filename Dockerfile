FROM public.ecr.aws/lambda/python:3.12

RUN mkdir -p /app

# Copy source code to working directory
COPY ./main.py /app/
COPY ./mylib /app/mylib/
COPY ./requirements.txt /app/requirements.txt

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Working Directory
WORKDIR /app
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]