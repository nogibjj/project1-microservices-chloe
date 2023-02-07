
FROM python

# Working directory
WORKDIR /app

# copy source code to the working directory
COPY . /app

# copy requirements.txt to the working directory
COPY requirements.txt .

# install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

# expose port 8080
EXPOSE 8080
    
CMD ["python", "app.py"] 