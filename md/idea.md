# python html framework

## 2 mods:
- compile
- terminal


## compile:
- store old version of files in a dictionnary
- compile the code if the file changed
- test every x seconds (set in the terminal mode)
- ctrl + c to exit compile mode

## .rdm.html

if empty rdm balise -> find the balise not empty in another file and replace the empty one with the not empty one

## .rdm.css
```css
label {
	color: red;
	input {
		display:hidden;
	}
}
```
->
```css
label {
	color: red;
}
label input {
	display:hidden;
}
```

# Cool feature I may add one day
- anchor balise wich take the id of the balise directly under it, change the id in the second balise then become
``<span class="marker" id="_"></span>``<br> the idea here is to move the position of the anchor that would point
on a balise so that it wouldn't be hidden under a header how much does it move have to be define inside the css
```css
.marker {
	position: relative;
	top: calc((-1) * var(--header-size));
}
```
- add a $ in front of sth to make it a temporary value, you can then remove all temporary values in the compiler's
console the regex to detect these temporary values is: ``\$["-Z]["-Z]* ?``
- template are block of code with arguments, you can then just call the template inside the file you've defined
it and specify the arguments so it will copy the template and fill the arguments
