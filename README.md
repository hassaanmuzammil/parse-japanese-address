# parse-japanese-address

Break down a japanese address to 5 levels:

- prefecture (県 都 府)
- city/ward/district/town (市 区 郡 町)
- town/area
- chome (丁目)
- banchi-go OR block-building (番地 - 号)

Example:
```
parse_japanese_address('大阪府大阪市港区築港3丁目5-9')

>>> ('大阪府', '大阪市港区', '築港', '3丁目', '5-9')
```
