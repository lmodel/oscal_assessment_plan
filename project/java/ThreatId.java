package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  A pointer, by ID, to an externally-defined threat.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThreatId  {

  private String href;
  private String system;
  private String id;

}