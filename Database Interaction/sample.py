@application.route("/post/vs_system", methods=['POST'])
def save_sys_data_vs():

    #print("Saving the VS system stats")
    payload = None
    if "m2m:nev" in request.json["m2m:sgn"]:
        payload = json.loads(request.json["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:cin"]["con"])

        vs_id        = payload['id']
        uptime       = payload['uptime']
        memory_usage = payload['mem_usage']
        disk_usage   = payload['disk_usage']
        ip           = payload['ip']
        cpu_usage    = payload['cpu']
        temperature  = payload['temp']

        sql_querry = "INSERT INTO vs_system (id_vs, ts, ip, cpu_usage, memory_usage, disk_usage, temperature, uptime) VALUES(%s, now(), %s, %s, %s, %s, %s, now() - to_timestamp(%s,'YY-MM-DD HH24:MI:SS'));"
        data = (vs_id, ip, cpu_usage, memory_usage, disk_usage, temperature, uptime)

        conn = psycopg2.connect(dbname=dbname, user=user, password=passwd, host=host, port=port)
        cur = conn.cursor()
        cur.execute(sql_querry, data)
        conn.commit()
        conn.close()

    return "", 200, {'X-M2M-RSC': '2000'}

@application.route("/")
def hello():
    log.debug(str(request.data))
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8182)
