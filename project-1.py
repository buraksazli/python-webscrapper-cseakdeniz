import urllib.request
#website url
url = "https://obs.akdeniz.edu.tr/oibs//bologna/progCourses.aspx?lang=en&curSunit=1040"

response = urllib.request.urlopen(url)

html_content = response.read()

html_string = html_content.decode()
end_index = 0
x = 1

for i in range(8):
    file_name = "Semester" + str(i+1) + ".txt"
    start_tag='<td width="20"><font face="Open Sans" color="#fff" size="1">'
    if i != 7:
        end_tag='<tr align="right" bgcolor="#454648">'
    else:
        end_tag='</table>'
    start_index = html_string.find(start_tag, end_index + len(end_tag)) 
    end_index = html_string.find(end_tag, start_index + len(start_tag))
    table_content = html_string[start_index:end_index + len(end_tag)]

    while 1==1:
        code_start_tag = '<span id="grdBolognaDersler_lblDersKod_' + str(x) + '">'
        name_start_tag = '<span id="grdBolognaDersler_lblDersAd_' + str(x) + '">'
        ects_start_tag = '<span id="grdBolognaDersler_lblAKTS_' + str(x) + '">'
        end_tag_2 = '</span>'
        
        code_start_index = table_content.find(code_start_tag)
        if code_start_index == -1:
            break
        code_end_index = table_content.find(end_tag_2, code_start_index + len(code_start_tag))
        name_start_index =  table_content.find(name_start_tag)
        name_end_index = table_content.find(end_tag_2, name_start_index + len(name_start_tag))
        ects_start_index =  table_content.find(ects_start_tag)
        ects_end_index = table_content.find(end_tag_2, ects_start_index + len(ects_start_tag))
        code_content = table_content[code_start_index:code_end_index + len(end_tag_2)]
        name_content = table_content[name_start_index:name_end_index + len(end_tag_2)]
        ects_content = table_content[ects_start_index:ects_end_index + len(end_tag_2)]
      
        start_tag_2='>'
        end_tag_2='<'
        code_start_index = code_content.find(start_tag_2, len(code_start_tag)) 
        code_end_index = code_content.find(end_tag_2,code_start_index)
        name_start_index = name_content.find(start_tag_2, len(name_start_tag))
        name_end_index = name_content.find(end_tag_2, name_start_index)
        ects_start_index = ects_content.find(start_tag_2, len(ects_start_tag))
        ects_end_index = ects_content.find(end_tag_2, ects_start_index)
        code_content = code_content[code_start_index + 1:code_end_index]
        name_content = name_content[name_start_index + 1:name_end_index]
        ects_content = ects_content[ects_start_index + 1:ects_end_index]
        
        if x == 103:
             x = x + 5
        elif x == 87:
            x = x + 7
        elif x == 57 or x == 73:
            x = x + 4
        elif x == 33 or x == 46:
            x = x + 2
        x = x + 1

        f = open(file_name, "a") 
        f.write(code_content + "  " + name_content + "  " + ects_content + "\n") 