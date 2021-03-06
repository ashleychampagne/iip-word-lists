DEFAULT_OUTPUT_NAME = "wordlist"
DEBUG = True 
TEI_NS = "{http://www.tei-c.org/ns/1.0}"
XML_NS = "{http://www.w3.org/XML/1998/namespace}"
IGNORE = ['⎜', '{', '}', '|', '(', '?', ')', ',', ';', '.', ':', 
           '"', "'", "<", ">", "+", "[", "]", "_", "/", "#", "*", '~', 
           '´', '=', '·', '‧', '⋅', '•', '∙']
INCLUDE_TRAILING_LINEBREAK = [TEI_NS + "persName", TEI_NS + "expan", 
                              TEI_NS + "choice", TEI_NS + "hi", TEI_NS +
                              "supplied", TEI_NS + "num", TEI_NS + 
                              "div", TEI_NS + "unclear", TEI_NS + "placeName"]
LATIN_CODES = ["la", "lat"]
GREEK_CODES = ["grc"]
codes = [
	["latin",["la", "lat"]],
	["hebrew",["heb", "he"]],
	["greek",["grc", "grk"]],
	["aramaic",["arc"]],
	["unknown", ["unk"]]
]

NUM_CONTEXT = 5

INFO_PAGE_HTML = """
<html>
	<head>
		<meta charset='UTF-8' />
		<script src="https://cdn.rawgit.com/google/code-prettify/master/loader/run_prettify.js"> </script>
		<link rel="stylesheet" type="text/css" href="../wordinfo.css"/>
	</head>
	<body>
		<h1></h1>
		<a id="doubletree-link" style="position: absolute; top: 20px; right: 20px;">Doubletree Visualization</a>
		<table>
			<tr>
				<td>Stem</td><td id='stem'></td>
			</tr>
			<tr>
				<td>Occurences: </td><td id='num-occurences'></td>
			</tr>
			<tr>
				<td>Total Frequency</td><td id='total-frequency'></td>
			</tr>
			<tr>
				<td>Language Frequency</td><td id='language-frequency'></td>
			</tr>
		</table>
		<h2>Variations</h2>
		<ul id='variations'>
		</ul>
		<!-- <h2>Files</h2>
		<ul id='files'>
		</ul> -->
		<h2>Regions</h2>
		<ul id='regions'>
		</ul>
		<!-- <iframe id='doubletree-frame' style='width: 100%; height: 400px;'>Your browser does not support frames.</iframe> -->
		<!-- <h2>Keyword in Context</h2>
		<ul id='kwic'></ul> -->
		<h2>Occurences</h2>
		<table id="occurences">
			<tr>
				<th>Variation</th>
				<th>File</th>
				<th>Word in Context</th>
				<th>XML</th>
				<th>Region</th>
				<th>Part of Speech</th>
			</tr>
		</table>
	</body>
</html>
""".replace("\t", "")

INDEX_PAGE_HTML = """
<html>
	<head>
		<meta charset='UTF-8' />
		<title></title>
		<script src="../levenshtein.min.js"> </script>
		<link rel="stylesheet" type="text/css" href="../style.css" />
	</head>
	<body>
		<!-- <h1></h1> -->
		<ul id='words'>
			<noscript id="wordList">
			
			</noscript>
		</ul>
		<script>
			wordsArray = [
				$WORDS_OBJECT
			];
		</script>
		<script src='../index_search.js'>   </script>
	</body>
</html>
""".replace("\t", "")

FRONT_PAGE_HTML = """
<html>
	<head>
		<meta charset='UTF-8' />
		<title>Language Selection</title>
	</head>
	<body>
		<h1>Languages</h1>
		<ul id='language-list-html'></ul>
	</body>
</html>
""".replace("\t", "")

OCCURENCE_TABLE_ROW_HTML = """
<tr>
	<td id="variation"></td>
	<td id="file"></td>
	<td id="kwic"></td>
	<td><code id="xml" class="prettyprint"></code></td>
	<td id="region"></td>
	<td id="pos"></td>
</tr>
""".replace("\t", "")
