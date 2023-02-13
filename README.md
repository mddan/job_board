# job_board
Job Board Data Camp ETL project 1 Group 4
# Editing from a template in progress ....

{{ Project Name }}

Project Plan

{{ Team Name }}

{{ Company Name }}

{{ Document Version }}

{{DATE}}

Revision History

| **Version** | **Author** | **Date** | **Description** |
|-------------|------------|----------|-----------------|
|             |            |          |                 |
|             |            |          |                 |
|             |            |          |                 |

Project Plan
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


This project aims to build a scalable and efficient ETL pipeline that can incrementally extract Jobs data 
(mainly data-related jobs like data analyst, data engineer, and data scientist) from an API. The project requires
a solution that can handle large amounts of data while ensuring the integrity and accuracy of the information. 
The product will be a centralized repository of live data that can be easily queried and analyzed. Using a Postgres database, 
we ensure that the data is stored in a structured and secure manner, allowing for efficient retrieval and manipulation of the information. 
The final result should be hosted on AWS, taking advantage of its various services to ensure the robustness and reliability of the pipeline. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
* ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
* ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
* ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GOAls -->
## GOALS

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* ??
  ```sh
  
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a Paid API Key at [https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch)
2. Clone the repo
   ```sh
   git clone  https://github.com/mddan/job_board.git
   ```
3. Install packages
   ```sh
   install requirements.txt
   ```
4. Enter your API in `???`
   ```
   API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

 
<!-- ROADMAP -->
## Roadmap

- [X] **`Data extraction:`**
    - [X] Set up API for data extraction 
    - [X] Retrieve the Jobs data from the API using a suitable extraction method (API calls)
    - [X] Set up live data update and incremental extract 
- [X] **`Data transformation:`**
    - [X] Clean the raw data to ensure it is in the desired format (e.g., removing duplicates, handling missing values, etc.).
    - [X] Use the following transformation techniques :  renaming columns, joining, grouping, typecasting, data filtering, sorting, and aggregating 
    - [X] Filter the data only to include the desired jobs (e.g., data analyst, data engineer, and data scientist).
    - [X] Transform the data into a structured format (e.g., converting to a tabular form or creating a data model).
- [X] **`Data loading:`**
    - [X] Create the necessary tables and schemas in the Postgres database to store the data
    - [X] Load the transformed data into the database.
    - [X] Use an efficient data loading method (e.g., upsert, etc.) to populate the database.
    - [X] Set up Incremental and upsert load
- [X] **`Create a data Pipeline`**
    - [X] Build a docker image using a Dockerfile
    - [X] Test that the Docker container is runing locally
- [X] **`Incremental extraction and loading:`**
    - [X] Set up a process to regularly extract new data from the API and update the database with the latest information.
    - [X] Ensure that the incremental process is designed to handle large amounts of data and maintain the integrity and accuracy of the information.
- [X] **`Implement unit tests`**
    - [X] Write pipeline metadata logs to a database table
- [X] **`Data Hosting :`**
    - [X] Host the database on AWS
    - [X] Use AWS services (e.g., RDS, EC2, S3, etc.) to ensure the robustness and reliability of the pipeline.

 
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

**Daniel Marinescu** - [@Linkedin](https://www.linkedin.com/in/danielmarinescu2/) 

**Vasanth Nair** - [@Linkedin](https://www.linkedin.com/in/vasanthnair/) 

**Christian Freeman** -  [@Linkedin](https://www.linkedin.com/in/christian-freeman-r/)

**Project Link:** [https://github.com/mddan/job_board](https://github.com/mddan/job_board)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
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
