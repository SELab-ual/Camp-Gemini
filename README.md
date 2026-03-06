# Camp - Gemini

## Proposed Sprint 1: Foundation and Core Entities

**1. Account Creation and Parent Onboarding**
You need users in the system before anything else can happen.

* As a parent I want to be able to create an account so that I can sign up my kids for camp online.


* As a camp administrator I want to be able to add parents so that they can enroll their kids at camp.



**2. Camper Registration and Enrollment**
Once parents exist in the system, they need to be able to add their children, or administrators need to do it for them.

* As a camp administrator I want to be able to add campers so that I can keep track of each individual camper.


* As a parent I want to be able to enroll my children so that they can be admitted to camp.



**3. Basic Organization**
Once campers are in the system, administrators need a way to organize them into manageable units.

* As a camp administrator I want to be able to create groups and add campers to the groups so that I can easily organize the campers.


## How to run



1. **Launch Docker:** Ensure Docker Desktop (or your Docker daemon) is running on your presentation machine.
2. **Build and Spin Up Containers:** Open your terminal, navigate to the folder containing your `docker-compose.yml`, and run:
```bash
docker-compose up --build -d

```


*(The `-d` flag runs it in detached mode so your terminal isn't cluttered, though you can run without it to monitor logs if preferred).*
3. **Verify the Services:** * Open `http://localhost` to ensure the Vue.js frontend loads.
* Open `http://localhost:8000/docs` to ensure the FastAPI backend is running and connected to the PostgreSQL database.
