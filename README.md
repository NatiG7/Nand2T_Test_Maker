<!-- Improved compatibility of back to top link: See:https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<h1>Custom Test maker for the Nand2Tetris(<a href=https://www.nand2tetris.org/"><strong>Nand2Tetris.org</strong></a>)</h1>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
***https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href=https://github.com/NatiG7/Nand2T_Test_Maker">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Nand2Tetris Gate Test Maker</h3>

  <p align="center">
    This is a test maker for the Nand2Tetris hardware simulator! <br><a href=https://www.nand2tetris.org/"><strong>Nand2Tetris Website</strong></a><br>
    Creates .tst and .cmp files and works with different logic gates, writes the tst files to match the standard tests in N2THWSim.
    <br />
    <a href="https://github.com/NatiG7/Nand2T_Test_Maker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href=https://github.com/NatiG7/Nand2T_Test_Maker">View Demo</a>
    ·
    <a href=https://github.com/NatiG7/Nand2T_Test_Maker/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href=https://github.com/NatiG7/Nand2T_Test_Maker/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]https://example.com)

Created to supply test and comparison files for non-built-in gates , for example the gate And3 / Or3.
Naturally they do not exist in the N2THWSim, this python script will prompt you for the necessary details
and create a formatted test file and the comparison file while checking how many variables, their interaction
and creating a truth table in the .cmp file that is aligned with boolean logic.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python.py]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The test maker uses a python script to receive information about
the gate you'd like to test.

Produces a .tst file that:
Loads the hdl file specified (Module_Name.hdl)
Compares to the created cmp file (Module_Name.cmp)
Creates an .out file for N2THWSim output (basically a truth table)
Applies formatting to the tables accordingly and sets inputs or outputs with all binary combinations for the number of inputs and/or outputs given.

Produces a cmp file that contains a truth table for the specified inputs and outputs (the N2THWSim applies the gate to the test cases)


### Prerequisites

[![Python][Python.py]][Python-url]<br>
Please refer to requirements.txt

### Installation

![installation]

* Clone this repo to a directory of your choice
* $ git clonehttps://github.com/NatiG7/Nand2T_Test_Maker.git
* $ pip install -r requirements.txt
* $ python Tstmkr1_0.py
* the created files will be written to the current directory the script will be at.
* After the script completes, you will have the {MODULE_NAME}.tst and {MODULE_NAME}.cmp files
* in the current directory to run with the hardware simulator.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

|![customgate]|![runscript]|
|---|---|
|![tstfile]|![cmpfile]|



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [1.0][✔] Creating Test Files for basic gates, NAND, NOT, AND, OR etc.
  - [1.0.1] Verify XOR,NOR,XNOR,MUX,DMUX
- [1.1] Add support for more complex gates
  - [1.1.1] Advanced logic application for gate types
  - [1.1.2] Ability to run multiple gate test creation
- [1.2] Implement HDL visualizer and create snapshots
    - [1.2.1] PravanJain's HDL Visualizer
    - [1.2.2] Create a local img file from the visualization
    - [1.2.3] Automatically append to tst file as an img comment
- [1.3] Implement Gate Logic builder for CUSTOM gate option

See the [open issues]https://github.com/NatiG7/Nand2T_Test_Maker/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nati G - Naticodeissues@proton.me

Project Link: https://github.com/NatiG7/Nand2T_Test_Maker]https://github.com/NatiG7/Nand2T_Test_Maker)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!--https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]:https://img.shields.io/github/contributors/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[contributors-url]:https://github.com/NatiG7/Nand2T_Test_Maker/graphs/contributors
[forks-shield]:https://img.shields.io/github/forks/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[forks-url]:https://github.com/NatiG7/Nand2T_Test_Maker/network/members
[stars-shield]:https://img.shields.io/github/stars/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[stars-url]:https://github.com/NatiG7/Nand2T_Test_Maker/stargazers
[issues-shield]:https://img.shields.io/github/issues/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[issues-url]:https://github.com/NatiG7/Nand2T_Test_Maker/issues
[license-shield]:https://img.shields.io/github/license/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[license-url]:https://github.com/NatiG7/Nand2T_Test_Maker/blob/master/LICENSE.txt
[product-screenshot]:images/screenshot.png
[Python.py]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]:https://www.python.org/
[customgate]:images/CustomAND3.png
[runscript]:images/ScriptOutput.png
[tstfile]:images/TstFileexample.png
[cmpfile]:images/cmpFileExample.png
[installation]:/images/install.png
