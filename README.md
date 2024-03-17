# 📚 Sound to Symphony (AI Music Generation)

- Generates completely new music by Recurrent Neural Network (RNN) that can be easily customizable by musical software
- Architectures RNN model for learning musica lpatterns from large classical music datasets that are expressed in numerical format.
- Deplyed the project into the Streamlit by utilizing FastAPI
- Built the connection between generated music and musical software Abelton
- [Demo day slide](https://github.com/MyoungchulK/Sound_To_Symphony_LeWgon/blob/main/slide/Sound_to_symphony_Le_Wagon.pdf) 
- [App home](https://sound-to-symphony-hggkk6gcyupalttasetpiw.streamlit.app/)

[sc1](https://github.com/MyoungchulK/Sound_To_Symphony_LeWgon/blob/main/slide/sc1.png)
[sc2](https://github.com/MyoungchulK/Sound_To_Symphony_LeWgon/blob/main/slide/sc2.png)
[sc3](https://github.com/MyoungchulK/Sound_To_Symphony_LeWgon/blob/main/slide/sc3.png)
   

## Getting Started
### Setup

Install gems
```
bundle install
```

### ENV Variables
Create `.env` file
```
touch .env
```
Inside `.env`, set these variables. For any APIs, see group Slack channel.
```
CLOUDINARY_URL=your_own_cloudinary_url_key
```

### DB Setup
```
rails db:create
rails db:migrate
rails db:seed
```

### Run a server
```
rails s
```

## Built With
- [Rails 7](https://guides.rubyonrails.org/) - Backend / Front-end
- [Stimulus JS](https://stimulus.hotwired.dev/) - Front-end JS
- [Heroku](https://heroku.com/) - Deployment
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Bootstrap](https://getbootstrap.com/) — Styling
- [Figma](https://www.figma.com) — Prototyping

## Acknowledgements
Inspired by Jane Mount's [Bibliophile](https://www.amazon.com/Bibliophile-Illustrated-Miscellany-Jane-Mount/dp/1452167230) and a story my father once told me: "Why do we keep books? ... We keep books because they remind us of the new perspectives and lessons we learned".

## Team Members
- [Douglas Berkley](https://www.linkedin.com/in/dougberkley/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License
