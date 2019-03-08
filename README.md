# sanic_benchmark

数据库表

```
CREATE TABLE `index_third_alternative` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `value` smallint(11) NOT NULL DEFAULT '0',
  `value_classification` varchar(11) COLLATE utf8mb4_unicode_ci DEFAULT '' COMMENT 'greed, fear',
  `timestamp` int(11) NOT NULL DEFAULT '0' COMMENT '平台的时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_alternative_timestamp` (`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

安装依赖
注意: 当前3.7.x 的aiohttp库有点 bug, 请用3.6.8测试
```
pip install -r requirements.txt
python main.py

```