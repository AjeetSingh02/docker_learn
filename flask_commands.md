* Hitting flask API in POST
	* curl -H "Content-Type:application/json" -X POST -d '{"input_file_path":"inputs/Store_POS.csv"}' http://localhost:5000/autoEDA

* To create requirements.txt using pipreqs package
	* pipreqs /user/flaskAPP          # /user/flaskAPP is the folder containing the scripts for whome you want to generate requirements.txt
	* pipreqs /user/flaskAPP --pypi-server http://infynp.ad.infosys.com/repository/pypi-all/simple      # Using custom proxy server
