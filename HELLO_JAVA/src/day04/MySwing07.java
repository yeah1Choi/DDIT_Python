package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 316, 289);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나:");
		lblMine.setBounds(61, 45, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴:");
		lblCom.setBounds(61, 92, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과:");
		lblResult.setBounds(61, 139, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(130, 42, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(130, 89, 116, 21);
		contentPane.add(tfCom);
		
		tfResult = new JTextField();
		tfResult.setColumns(10);
		tfResult.setBounds(130, 136, 116, 21);
		contentPane.add(tfResult);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(61, 186, 185, 23);
		contentPane.add(btn);
	}
	void myClick() {
		String mine = tfMine.getText();
		String com = "";
		String result = "";
		
		double rnd = Math.random();
		
		if(rnd < 0.33) {
			com = "가위";
		} else if(rnd < 0.66) {
			com = "바위";
		} else {
			com = "보";
		}
		
		tfCom.setText(com);
		
		if (mine.equals(com)) {
			result = "비겼습니다";
		} else if(mine.equals("가위") && com.equals("보")) {
			result = "이겼습니다"; 
		} else if(mine.equals("바위") && com.equals("가위")) {
			result = "이겼습니다"; 
		} else if(mine.equals("보") && com.equals("바위")) {
			result = "이겼습니다"; 
		} else {
			result = "졌습니다";
		}
		
		tfResult.setText(result);
		
	}
}
