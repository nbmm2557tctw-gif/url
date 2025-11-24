# Cloudflare DDNS 一鍵部署包

## 使用方式

1. 將整個資料夾上傳到伺服器。
2. 編輯 `config.json`，填入你的 Cloudflare API Token、Zone ID、Record Name。
3. 執行部署：
```bash
chmod +x setup.sh
./setup.sh
```
4. DDNS 將自動每 5 分鐘更新，日誌寫入 `ddns.log`。
5. 將 `test.php` 放到網頁目錄測試 PHP 是否成功。
