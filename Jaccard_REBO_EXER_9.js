        //Variables
        let t1 = document.getElementById("text1");
        let t2 = document.getElementById("text2");
        let t3 = document.getElementById("caja3");
        let c2 = document.getElementById("img");

        //DOM Management
        //1)
        t1.addEventListener('mouseover', function(){
            t2.style.display = "none";
        })
        t1.addEventListener('mouseout', function(){
            t2.style.display = "block";
        })

        //2)
        c2.addEventListener('click', function(){
            c2.style.width = "100%";
        })
        c2.addEventListener('mouseout', function(){
            c2.style.width = "20%";
        })

        //3)
        t3.addEventListener('dblclick', function(){
            t3.style.fontSize = "30px";
        })