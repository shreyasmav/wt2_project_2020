(function ($) {
    "use strict";

foo:function()
		{
			//var obj1=new firstfoo();

			var e=document.getElementById("cell");
			var value="no action";
			console.log(value);
			xhr=new XMLHttpRequest();
			//xhr.timeout=5000;
			//xhr.ontimeout=obj.backoff;
			
			xhr.onreadystatechange=obj1.firstfoo;
			xhr.send()


		},
		firstfoo:function()
		{
			if(this.readyState==4 && this.status==200)
				{
					var data=this.responseText;
					var list=data.split(".");

					document.getElementById("cse").innerHTML=list[0]
					document.getElementById("ece").innerHTML=list[1]
					document.getElementById("me").innerHTML=list[2]
					document.getElementById("cv").innerHTML=list[3]
					document.getElementById("eee").innerHTML=list[4]
				}
		}

	}
	setInterval(obj1.foo,2000);
		function init()
		{
			obj=new Data();
			obj.getData();
			c=setInterval(obj.showScore,5000);
		}
		function Data()
		{
			this.getData=function()
			{
				var e=document.getElementById("cell");
				var value=e.options[e.selectedIndex].value;
				console.log(value);
				xhr=new XMLHttpRequest();
				xhr.timeout=5000;
				xhr.ontimeout=obj.backoff;
				xhr.open("GET","http://localhost/week6/seat.php?value="+value,true)
				xhr.onreadystatechange=obj.showScore
				xhr.send()
			}
			this.backoff=function()
			{
				console.log("no response");
				n=n*2;
				console.log("n=",n);
				setTimeout(this.getData, n*1000);
			}
			this.showScore=function()
			{
				
				if(this.readyState==4 && this.status==200)
				{
					console.log("i");
					var data=this.responseText;
					var list=data.split(".");

					document.getElementById("cse").innerHTML=list[0]
					document.getElementById("ece").innerHTML=list[1]
					document.getElementById("me").innerHTML=list[2]
					document.getElementById("cv").innerHTML=list[3]
					document.getElementById("eee").innerHTML=list[4]
					//xhr.abort();
					n=2;
				}
			}

		}
		document.addEventListener('DOMContentLoaded', function() {
		var elems = document.querySelectorAll('select');
		var instances = M.FormSelect.init(elems, {});
	});


      updateClock();
      var timeinterval = setInterval(updateClock, 1000);
    }

    var deadline = new Date(Date.parse(new Date()) + 25 * 24 * 60 * 60 * 1000 + 13 * 60 * 60 * 1000); 
    initializeClock('clockdiv', deadline);

})(jQuery);
