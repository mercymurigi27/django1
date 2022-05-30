const copyBtns = document.querySelectorAll('.copy');


copyBtns.forEach(function(btn) {

    btn.addEventListener('click', () => {
        const link = btn.nextElementSibling;
        const data = [new ClipboardItem({ "text/plain": new Blob([link.innerText], { type: "text/plain" }) }) ]
      
       navigator.clipboard.write(data).then(
           function(){
               alert('link Copied to clipboard')
           },function(){
               alert('error, please try again')
           })
    })
})

