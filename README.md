git clone https://github.com/zaazouamouad/toolkit.git
cd toolkit

apt update && apt install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python3 nexu.py
