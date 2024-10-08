package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "os/exec"
    "strconv"
    "strings"
    "time"
)

type Info struct {
    IPAddress  string `json:"ip_address"`
    Processes  string `json:"processes"`
    DiskSpace  string `json:"disk_space"`
    Uptime     string `json:"uptime"`
}


func formatUptime(seconds string) string {
    uptimeSeconds, _ := strconv.ParseFloat(seconds, 64)
    duration := time.Duration(uptimeSeconds) * time.Second
    days := int(duration.Hours() / 24)
    hours := int(duration.Hours()) % 24
    minutes := int(duration.Minutes()) % 60

    return fmt.Sprintf("up %d days, %d hours, %d minutes", days, hours, minutes)
}

func getContainerInfo() Info {

    ip, _ := exec.Command("sh", "-c", "ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1").Output()
    ipAddress := strings.TrimSpace(string(ip))


    ps, _ := exec.Command("ps", "aux").Output()
    processes := string(ps)

    df, _ := exec.Command("df", "-h", "/").Output()
    diskSpace := string(df)

  
    uptimeData, _ := ioutil.ReadFile("/proc/uptime")
    uptimeSeconds := strings.Fields(string(uptimeData))[0]
    uptime := formatUptime(uptimeSeconds)

    return Info{
        IPAddress: ipAddress,
        Processes: processes,
        DiskSpace: diskSpace,
        Uptime:    uptime,
    }
}

func handler(w http.ResponseWriter, r *http.Request) {
    info := getContainerInfo()

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(info)
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Service2 running on port 5000...")
    http.ListenAndServe(":5000", nil)
}
