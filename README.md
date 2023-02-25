# parse-japanese-address

Break down a japanese address to 5 levels:

- prefecture 
- city/ward/district/town (市区郡町)
- town/area
- chome (丁目)
- banchi-go OR block-building (番地-号)

Example:
```
parse_japanese_address('大阪府大阪市港区築港3丁目5-9')

>>> ('大阪府', '大阪市港区', '築港', '3丁目', '5-9')
```
