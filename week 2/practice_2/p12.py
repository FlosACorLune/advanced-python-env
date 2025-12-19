text = "Cras aliquetI aliquamI nulla et cursus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aliquam erat volutpat. Nulla id libero sit amet nisl sagittis ultrices nec sed magna. Sed dignissim congue ipsum. Proin iaculis tellus luctus risusI ultrices volutpat. Nullam tortor est, varius sit amet enim et, maximus fringilla neque. Phasellus imperdiet magna in dui sodales, vitae elementum mauris malesuada. Morbi turpis enim, laoreet ut ullamcorper id, auctor in dui. Fusce hendrerit ex vitae augue scelerisque ullamcorper. Cras sed nibh id leo consequat molestie. Vestibulum eu sodales massa. Donec tincidunt neque nec nulla consequat egestas.I"

count=0
new_text = text.split()
for i in range(len(new_text)):
    if new_text[i].endswith('I'):
        count+=1
print(count)