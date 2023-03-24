"""
Aplikasi membuat modularisasi Berita terkini dari kompas TV

"""

import news

if __name__ == '__main__':
        print("main application")
        result = news.data_extraction()
        news.data_show(result)
