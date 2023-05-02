import pytest
from main import gen_url,get_rp,export_uf_a_csv,import_uf_array,comp_file,main
 
@pytest.mark.parametrize(
	["aa","r"],
	[
    	("2018","https://www.sii.cl/valores_y_fechas/uf/uf2018.htm"),
    	("2019","https://www.sii.cl/valores_y_fechas/uf/uf2019.htm"),
    	("2023","https://www.sii.cl/valores_y_fechas/uf/uf2023.htm"),
    ],
)

def test_gen_url(aa,r):
	assert gen_url(aa) == r

@pytest.mark.parametrize(
	["url","r"],
	[
    	("https://www.sii.cl/valores_y_fechas/uf/uf2018.htm",404),
    	("https://www.sii.cl/valores_y_fechas/uf/uf2019.htm",404),
    	("https://www.sii.cl/valores_y_fechas/uf/uf2023.htm",404),
    ],
)

def test_get_rp(url,r):
	assert get_rp(url) != r

@pytest.mark.parametrize(
	["url","f","r"],
	[
    	("https://www.sii.cl/valores_y_fechas/uf/uf2018.htm","./repo/2023.csv",404),
    	("https://www.sii.cl/valores_y_fechas/uf/uf2023.htm","./repo/2023.csv",404),
    ],
)

def test_export_uf_a_csv(url,f,r):
	assert export_uf_a_csv(url,f) != r

@pytest.mark.parametrize(
	["dd","mm","aa","f","r"],
	[
    	(1,12,2028,"./repo/2023.csv",404),
    ],
)

def test_import_uf_array(dd,mm,aa,f,r):
	assert import_uf_array(dd,mm,aa,f) != r

@pytest.mark.parametrize(

	["url","f","r"],
	[
    	("https://www.sii.cl/valores_y_fechas/uf/uf2023.htm","./repo/2023.csv",404),
    ],
)

def test_comp_file(url,f,r):
	assert comp_file(url,f) != r

@pytest.mark.parametrize(

	["f","r"],
	[
    	("11-11-2022",404),
    ],
)

def test_main(f,r):
	assert main(f) != r
