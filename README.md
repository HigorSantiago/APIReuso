Este projeto é para a cadeira de Reuso de Softwre com a finalidade de uma construção de uma API RESTful para gerenciar informações de cursos em
uma plataforma educacional. 

# Instalar Dependencias 

pip install fastapi uvicorn


# Executar a API 
python -m uvicorn api_cursos_cliente:app --reload


# Testar o Cliente 
python api_cursos_cliente.py


# Testar API Manualmente 
http://127.0.0.1:8000/docs
