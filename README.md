# East-Vantage-Assigment

## Steps to get started locally

### Step 1

- Clone repo by using

```
git clone https://github.com/fabpot11/East-Vantage-Assigment.git
```

### Step 2

- Go to main file

```
cd East-Vantage-Assigment
```

### Step 3

- Create a environment in your system using

```
virtualenv nameOfEnv
```

### Step 4

- Activate environment using

```
source nameOfEnv/bin/activate
```

### Step 5

- Install all requirements from requirements.txt file using

```
pip install -r requirements.txt
```

### Step 6

- In terminal run

```
uvicorn index:app --port {PORTNUMBER} --reload
```

### Step 7

- Hit This Url

```
http://127.0.0.1:PORTNUMBER/docs
```
