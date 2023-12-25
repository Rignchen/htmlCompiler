# algo
1. split ``<model/>`` 
2. put each model part inside the content at the right place and fuse it with both sides
3. fuse the content back to get 1 string

# test

## step 1
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<model/>
</body>
</html>
```
\+ [
```html
<article>
	<section>
		<model/>
	</section>
	<section>
		<model/>
	</section>
	<section>
		<model/>
	</section>
</article>
```
]
->
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<article>
	<section>
		<model/>
	</section>
	<section>
		<model/>
	</section>
	<section>
		<model/>
	</section>
</article>
</body>
</html>
```
## step 2
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<article>
	<section>
		<model/>
	</section>
	<section>
		<model/>
	</section>
	<section>
		<model/>
	</section>
</article>
</body>
</html>
```
\+ [
```html
<div>
	<span>
		pomme
	</span>
</div>
```
```html
<div>
	<span>
		poire
	</span>
</div>
```
] ->
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<article>
	<section>
		<div>
	<span>
		<model/>
	</span>
</div>
	</section>
	<section>
		<div>
	<span>
		<model/>
	</span>
</div>
	</section>
	<section>

	</section>
</article>
</body>
</html>
```
## step 3

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<article>
	<section>
		<div>
	<span>
		<model/>
	</span>
</div>
	</section>
	<section>
		<div>
	<span>
		<model/>
	</span>
</div>
	</section>
	<section>

	</section>
</article>
</body>
</html>
```
\+ [
```html
pomme
```
```html
poire
```
```html
abricot
```
] ->
```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<article>
	<section>
		<div>
	<span>
		pomme
	</span>
</div>
	</section>
	<section>
		<div>
	<span>
		poire
	</span>
</div>
	</section>
	<section>

	</section>
</article>
</body>
</html>
```