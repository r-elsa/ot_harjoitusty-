```mermaid
 classDiagram
      UI -->  Services
      Entities -- Services
      Services --> Repositories
      Repositories --> Entities
      class Services{
          class User Service
          class Tweet Service
          class Like Service
      }
      class UI{
          class UI
      }
      class Entities {
        class User
        class Tweet
        class Like
      }
      class Repositories{
      
      
      }
```
