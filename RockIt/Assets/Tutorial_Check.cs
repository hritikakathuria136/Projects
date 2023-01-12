using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Tutorial_Check : MonoBehaviour
{
    public void goToLevel()
    {
        SceneManager.LoadScene("Tutorial_Check");
    }
}
