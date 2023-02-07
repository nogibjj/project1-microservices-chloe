
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
    
CMD ["python", "app.py"] 