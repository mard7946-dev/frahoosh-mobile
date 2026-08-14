package ir.frahoosh.mobile

import android.app.Activity
import android.graphics.Color
import android.os.Bundle
import android.view.Gravity
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast

class MainActivity : Activity() {

    private val orange = Color.rgb(245, 158, 11)
    private val green = Color.rgb(22, 163, 74)
    private val dark = Color.rgb(30, 30, 30)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        showLogin()
    }

    private fun showLogin() {

        val root = LinearLayout(this)
        root.orientation = LinearLayout.VERTICAL
        root.gravity = Gravity.CENTER
        root.setPadding(50, 50, 50, 50)
        root.setBackgroundColor(Color.rgb(248, 250, 252))

        val title = TextView(this)
        title.text = "فراهوش"
        title.textSize = 34f
        title.setTextColor(orange)
        title.gravity = Gravity.CENTER

        val subtitle = TextView(this)
        subtitle.text = "سامانه هوشمند آموزشی یکپارچه"
        subtitle.textSize = 17f
        subtitle.setTextColor(dark)
        subtitle.gravity = Gravity.CENTER

        val username = EditText(this)
        username.hint = "نام کاربری"
        username.textSize = 17f
        username.setSingleLine(true)

        val password = EditText(this)
        password.hint = "رمز عبور"
        password.textSize = 17f
        password.setSingleLine(true)
        password.inputType =
            android.text.InputType.TYPE_CLASS_TEXT or
            android.text.InputType.TYPE_TEXT_VARIATION_PASSWORD

        val loginButton = Button(this)
        loginButton.text = "ورود به فراهوش"
        loginButton.textSize = 17f
        loginButton.setTextColor(Color.WHITE)
        loginButton.setBackgroundColor(green)

        val version = TextView(this)
        version.text = "نسخه موبایل فراهوش 1.0.0"
        version.textSize = 13f
        version.setTextColor(Color.GRAY)
        version.gravity = Gravity.CENTER

        root.addView(
            title,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
        )

        root.addView(
            subtitle,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            )
        )

        root.addView(
            username,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 60
            }
        )

        root.addView(
            password,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 15
            }
        )

        root.addView(
            loginButton,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 25
            }
        )

        root.addView(
            version,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 35
            }
        )

        loginButton.setOnClickListener {

            val user = username.text.toString().trim()
            val pass = password.text.toString()

            if (user.isEmpty() || pass.isEmpty()) {

                Toast.makeText(
                    this,
                    "نام کاربری و رمز عبور را وارد کنید",
                    Toast.LENGTH_SHORT
                ).show()

                return@setOnClickListener
            }

            showDashboard(user)
        }

        setContentView(root)
    }

    private fun showDashboard(username: String) {

        val root = LinearLayout(this)
        root.orientation = LinearLayout.VERTICAL
        root.gravity = Gravity.CENTER
        root.setPadding(40, 40, 40, 40)
        root.setBackgroundColor(Color.rgb(248, 250, 252))

        val title = TextView(this)
        title.text = "داشبورد فراهوش"
        title.textSize = 30f
        title.setTextColor(orange)
        title.gravity = Gravity.CENTER

        val welcome = TextView(this)
        welcome.text = "خوش آمدید\n$username"
        welcome.textSize = 20f
        welcome.setTextColor(dark)
        welcome.gravity = Gravity.CENTER

        val updateButton = Button(this)
        updateButton.text = "بررسی به‌روزرسانی"
        updateButton.textSize = 17f

        val logoutButton = Button(this)
        logoutButton.text = "خروج"
        logoutButton.textSize = 17f

        root.addView(title)

        root.addView(
            welcome,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 30
            }
        )

        root.addView(
            updateButton,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 50
            }
        )

        root.addView(
            logoutButton,
            LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT
            ).apply {
                topMargin = 15
            }
        )

        updateButton.setOnClickListener {
            Toast.makeText(
                this,
                "سیستم به‌روزرسانی فراهوش آماده است",
                Toast.LENGTH_SHORT
            ).show()
        }

        logoutButton.setOnClickListener {
            showLogin()
        }

        setContentView(root)
    }
}
