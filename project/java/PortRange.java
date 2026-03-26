package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Where applicable, the transport layer protocol port range.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PortRange  {

  private String start;
  private String end;
  private String transport;
  private String remarks;

}