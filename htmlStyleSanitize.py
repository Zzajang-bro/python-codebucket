# 20230806
# htmlStyleSanitize( 문자열 ) => 특수기호를 앰퍼샌드로 바꾼 문자열

def htmlStyleSanitize( damn_str ):
	damn_str = damn_str.replace('&', '&amp;')
	damn_str = damn_str.replace('<', '&lt;')
	damn_str = damn_str.replace('>', '&gt;')
	damn_str = damn_str.replace(' ', '&nbsp;')
	damn_str = damn_str.replace('"', '&quot;')
	damn_str = damn_str.replace("'", '&apos;')
	damn_str = damn_str.replace('¢', '&cent;')
	damn_str = damn_str.replace('£', '&pound;')
	damn_str = damn_str.replace('¥', '&yen;')
	damn_str = damn_str.replace('€', '&euro;')
	damn_str = damn_str.replace('©', '&copy;')
	damn_str = damn_str.replace('®', '&reg;')
	damn_str = damn_str.replace('\n', '<br>')
	return damn_str