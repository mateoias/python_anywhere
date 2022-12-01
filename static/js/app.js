

function sendUserInput() {
  let userinput = document.getElementById('userinput').value
  console.log(userinput)
  const request = new XMLHttpRequest()
  request.open('POST', `/getUserInput/${JSON.stringify(userinput)}`)
  request.send()
  // const article_text = {{ text|tojson }}
  console.log(userinput);
}