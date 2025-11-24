#!/bin/bash

echo "=== 開始部署 Cloudflare DDNS 與 PHP 環境 ==="

# 更新套件
sudo apt update -y && sudo apt upgrade -y

# 安裝 PHP
sudo apt install -y php-cli php-curl

# 安裝 Python 與 pip
sudo apt install -y python3 python3-pip
pip3 install requests

# 建立 DDNS 目錄
mkdir -p ~/cloudflare_ddns
cd ~/cloudflare_ddns

# 複製範例 config
if [ ! -f config.json ]; then
    cp ../config.json.example ./config.json
    echo "請編輯 config.json 填入你的 Cloudflare 資訊"
fi

# 設定可執行權限
chmod +x ddns.py

# 設定 cron 每 5 分鐘自動執行
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/bin/python3 $HOME/cloudflare_ddns/ddns.py >> $HOME/cloudflare_ddns/ddns.log 2>&1") | crontab -

echo "=== 部署完成！DDNS 將每 5 分鐘自動更新 ==="
