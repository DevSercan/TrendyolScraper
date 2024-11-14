import requests
from bs4 import BeautifulSoup
from src.utils.helper import removeSuffix
from src.classes.Log import Log
import time

log = Log()

class Trendyol:
    def __init__(self):
        try:
            self.headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cache-Control': 'max-age=0',
                'Priority': 'u=0, i',
                'Sec-Ch-Ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
            }
        except Exception as e:
            log.error(f"Unexpected error in '__init__' function of the 'Trendyol' class:\n{e}")
    
    def _getResponse(self, url):
        """ HTTP GET İşlemini gerçekleştirerek yanıtı döndürür. """
        while True:
            try:
                with requests.session() as session:
                    response = session.get(url=url, headers=self.headers, timeout=10)
                    return response
            except Exception as e:
                log.error(f"Unexpected error in '_getResponse' function of the 'Trendyol' class:\n{e}")
                time.sleep(1)
    
    def getFollowerCount(self, sellerId):
        try:
            log.debug(f"[sellerId={sellerId}] The 'getFollowerCount' function of the 'Trendyol' class has been executed.")
            url = f"https://public.trendyol.com/discovery-sellerstore-webgw-service/v1/follow/?sellerId={sellerId}&culture=tr-TR&channelId=1"
            response = self._getResponse(url)
            if response.status_code == 200:
                return int(response.json()["count"])
            else:
                log.debug(f"[sellerId={sellerId}] The status code of the 'getFollowerCount' function is {response.status_code}")
                return None
        except Exception as e:
            log.error(f"[sellerId={sellerId}] Unexpected error in 'getFollowerCount' function of the 'Trendyol' class:\n{e}")
            return None
        finally:
            log.debug(f"[sellerId={sellerId}] The 'getFollowerCount' function of the 'Trendyol' class has completed.")
    
    def getStoreName(self, sellerId):
        try:
            log.debug(f"[sellerId={sellerId}] The 'getStoreName' function of the 'Trendyol' class has been executed.")
            url = f"https://public.trendyol.com/discovery-sellerstore-webgw-service/v1/seller-store/header?culture=tr-TR&storefrontId=1&supplierId={sellerId}&sellerStoreFrom=Profile&channelId=1"
            response = self._getResponse(url)
            if response.status_code == 200:
                html = response.json()["result"]["html"]
                soup = BeautifulSoup(html, 'lxml')
                storeName = soup.find('h1', class_='seller-store__name').text
                return storeName
            else:
                log.debug(f"[sellerId={sellerId}] The status code of the 'getStoreName' function is {response.status_code}")
                return None
        except Exception as e:
            log.error(f"[sellerId={sellerId}] Unexpected error in 'getStoreName' function of the 'Trendyol' class:\n{e}")
            return None
        finally:
            log.debug(f"[sellerId={sellerId}] The 'getStoreName' function of the 'Trendyol' class has completed.")
    
    def getCategories(self, sellerId):
        try:
            log.debug(f"[sellerId={sellerId}] The 'getCategories' function of the 'Trendyol' class has been executed.")
            url = f"https://apigw.trendyol.com/discovery-sellerstore-webgw-service/v1/search/aggregations?merchantId={sellerId}&culture=tr-TR&channelId=1"
            response = self._getResponse(url)
            categoryList = []
            if response.status_code == 200:
                categories = response.json()["categories"]
                for category in categories:
                    categoryList.append(category["text"])
                return categoryList
            else:
                log.debug(f"[sellerId={sellerId}] The status code of the 'getCategories' function is {response.status_code}")
                return None
        except Exception as e:
            log.error(f"[sellerId={sellerId}] Unexpected error in 'getCategories' function of the 'Trendyol' class:\n{e}")
            return None
        finally:
            log.debug(f"[sellerId={sellerId}] The 'getCategories' function of the 'Trendyol' class has completed.")
    
    def getStoreLocation(self, sellerId):
        try:
            log.debug(f"[sellerId={sellerId}] The 'getStoreLocation' function of the 'Trendyol' class has been executed.")
            url = f"https://trendyol.com/magaza/profil/magaza-m-{sellerId}?sk=1&channelId=1&language=tr"
            response = self._getResponse(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                storeLocation = soup.find_all('span', class_='seller-info-container__wrapper__text-container__value')[1].text.strip()
                return storeLocation
            else:
                log.debug(f"[sellerId={sellerId}] The status code of the 'getStoreLocation' function is {response.status_code}")
                return None
        except Exception as e:
            log.error(f"[sellerId={sellerId}] Unexpected error in 'getStoreLocation' function of the 'Trendyol' class:\n{e}")
            return None
        finally:
            log.debug(f"[sellerId={sellerId}] The 'getStoreLocation' function of the 'Trendyol' class has completed.")
    
    def isStoreAvailable(self, sellerId):
        try:
            log.debug(f"[sellerId={sellerId}] The 'isStoreAvailable' function of the 'Trendyol' class has been executed.")
            url = f"https://apigw.trendyol.com/discovery-sellerstore-webgw-service/v1/seller-store/header?culture=tr-TR&storefrontId=1&supplierId={sellerId}&sellerStoreFrom=Profile&channelId=1"
            response = self._getResponse(url)
            if response.status_code == 200:
                return True
            else:
                log.debug(f"[sellerId={sellerId}] The status code of the 'isStoreAvailable' function is {response.status_code}")
                return False
        except Exception as e:
            log.error(f"[sellerId={sellerId}] Unexpected error in 'isStoreAvailable' function of the 'Trendyol' class:\n{e}")
            return False
        finally:
            log.debug(f"[sellerId={sellerId}] The 'isStoreAvailable' function of the 'Trendyol' class has completed.")