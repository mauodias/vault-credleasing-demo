
read -p "[?] Are you sure you want to remove all Vault's data (y/n)? " answer
case ${answer:0:1} in
    y|Y )
        echo "[*] Removing files..."
        rm -rf ./_data/consul
        rm -rf ./_data/postgres
        docker-compose down
    ;;
    * )
        echo "[*] Aborting..."
    ;;
esac
