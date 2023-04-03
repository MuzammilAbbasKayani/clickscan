# Clickscan
Clickscan is a Python command-line tool that scans a list of subdomains for the presence of the X-Frame-Options header. The X-Frame-Options header is a security feature that prevents clickjacking attacks by denying the rendering of a page in a frame or iframe. If the header is missing, the page may be vulnerable to clickjacking.

## Requirements
Clickscan requires Python 3.x and the requests module to be installed. You can install requests using pip:

Copy code
<code>pip install requests</code>
## Usage
To use Clickscan, simply run the script and pass in a file containing a list of subdomains to scan:
<code>python clickjacking_finder.py subdomains.txt</code>
The script will scan each subdomain and print out whether or not it is vulnerable to clickjacking. 
For example:

<code>$ python clickscan.py subdomains.txt
example.com is not vulnerable to Clickjacking
subdomain.example.com is vulnerable to Clickjacking
</code>
By default, Clickscan will use 10 threads to scan the subdomains simultaneously. You can adjust this number by modifying the THREADS constant at the top of the script.

Contributing
Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.
