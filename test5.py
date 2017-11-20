html_str = """<html>
	<body>
		<div id="main" class="section">
			<span><h2>Hello, 206!</h2></span>
			<a href="http://piazza.com">Piazza</a>
		</div>
		<div id="secondary" class="section">
			<ol>
				<li><a href="http://umich.edu">UM</a></li>
				<li>This one is just text.</li>
			</ol>
		</div>
	</body>
</html>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_str,'html.parser')
lst = soup.find_all('a')
for element in lst:
	print((element['href'])	


for in x: