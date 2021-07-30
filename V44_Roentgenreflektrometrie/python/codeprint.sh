#!/bin/bash

input_file=$1

filename=$(basename -- "${input_file}")
filename="${filename%.*}"

output_filename="${filename}.pdf"

output_directory=/tmp/codeprint-$(date --iso)/

mkdir -p "${output_directory}"

tmpfile="${output_directory}/codeprint.tex"

echo "
\\documentclass{scrartcl}
\\usepackage{minted}
\\begin{document}
\\section*{\\texttt{${input_file//_/\\_}\\\\$(date -Iminutes)}}
\\inputminted[linenos,breaklines]{python}{${input_file}}
\\end{document}
" > "${tmpfile}"

lualatex \
    --interaction=batchmode \
    --shell-escape \
    --output-directory="${output_directory}" \
    "${tmpfile}" > /dev/null

cp "${tmpfile%.*}.pdf" "${output_filename}"
rm -rf "${output_directory}"

echo "Created ${output_filename}"
