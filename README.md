# dirty_code

alias ll='ls -l'
alias gfp='git fetch --prune'
alias gl1='git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit'
alias gl2='git log --graph --abbrev-commit --decorate --format=format:''%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)'' --all'
alias gl3='git log --graph --abbrev-commit --decorate --format=format:''%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
alias gl=gl1
alias mvntest='export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8; ./mvnw -Dspring-boot.run.arguments="--logging.level.org.hibernate.SQL=ERROR --logging.level.org.hibernate.type.descriptor.sql=ERROR --logging.level.org.springframework.orm.jpa=ERROR --logging.level.com.fastretailing.marketingpf=ERROR --logging.level.org.springframework.security=ERROR --spring.datasource.url=jdbc:postgresql://localhost:5432/fr_mkpf_test?sslmode=disable" clean test clean eclipse:eclipse'
alias mvntest2='export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8; ./mvnw -Dspring-boot.run.arguments="--logging.level.org.hibernate.SQL=ERROR --logging.level.org.hibernate.type.descriptor.sql=ERROR --logging.level.org.springframework.orm.jpa=ERROR --logging.level.com.fastretailing.marketingpf=ERROR --logging.level.org.springframework.security=ERROR --spring.datasource.url=jdbc:postgresql://localhost:5432/fr_mkdb?sslmode=disable" clean test clean eclipse:eclipse'
alias fl='for i in {1..360}
do
	read -p "Enter to fetch: " number_of_commit
    echo "fetching... ${number_of_commit}"
    gfp;
    clear;
    date;
    git log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit --all -${number_of_commit:-10};
done'
alias dbt='_dbt(){ MODEL_SELECTOR="$1" docker-compose --env-file prd.txt -f docker-compose-dbt-test.yml up;}; _dbt'
HISTSIZE=20000
HISTFILESIZE=20000
