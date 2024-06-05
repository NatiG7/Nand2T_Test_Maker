<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<h1>UNDER CONSTRUCTION!</h1>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/NatiG7/Nand2T_Test_Maker">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Nand2Tetris Gate Test Maker</h3>

  <p align="center">
    This is a test maker for the Nand2Tetris hardware simulator!
    Creates .tst and .cmp files and works with different logic gates, writes the tst files to match the standard tests in N2THWSim.
    <br />
    <a href="https://github.com/NatiG7/Nand2T_Test_Maker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NatiG7/Nand2T_Test_Maker">View Demo</a>
    ·
    <a href="https://github.com/NatiG7/Nand2T_Test_Maker/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/NatiG7/Nand2T_Test_Maker/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

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

* Latest version of python.

### Installation

* Clone this repo to a directory of your choice
* Run Tstmkr1.0.py
* the created files will be written to the current directory the script will be at.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [1.0] Creating Test Files for basic gates, NAND, NOT, AND, OR etc.
- [1.1] Add support for more complex gates
  - [1.1.1] Advanced logic application for gate types
  - [1.1.2] Ability to run multiple gate test creation
- [1.2] Implement HDL visualizer and create snapshots
    - [1.2.1] PravanJain's HDL Visualizer
    - [1.2.2] Create a local img file from the visualization
    - [1.2.3] Automatically append to tst file as an img comment
- [1.3] Implement Gate Logic builder for CUSTOM gate option

See the [open issues](https://github.com/NatiG7/Nand2T_Test_Maker/issues) for a full list of proposed features (and known issues).

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

Nati G - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/NatiG7/Nand2T_Test_Maker](https://github.com/NatiG7/Nand2T_Test_Maker)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[contributors-url]: https://github.com/NatiG7/Nand2T_Test_Maker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[forks-url]: https://github.com/NatiG7/Nand2T_Test_Maker/network/members
[stars-shield]: https://img.shields.io/github/stars/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[stars-url]: https://github.com/NatiG7/Nand2T_Test_Maker/stargazers
[issues-shield]: https://img.shields.io/github/issues/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[issues-url]: https://github.com/NatiG7/Nand2T_Test_Maker/issues
[license-shield]: https://img.shields.io/github/license/NatiG7/Nand2T_Test_Maker.svg?style=for-the-badge
[license-url]: https://github.com/NatiG7/Nand2T_Test_Maker/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Python.py]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]:https://www.python.org/
